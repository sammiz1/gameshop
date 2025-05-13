from models import db
from sqlalchemy import text

class Game:
    def get(flag='discount', offset=0, limit=10):
        if flag == 'discount':
            q = f"""
                SELECT * from (SELECT ag.* from all_games ag 
                order by ag.perc_discount DESC 
                limit {limit} offset {offset}) sbgames 
                left join favgames f on f.game_id = sbgames.row_id
            """
        elif flag == 'trending':
            q = f"""
                SELECT * from (SELECT ag.* from all_games ag 
                order by ag.clean_price DESC 
                limit {limit} offset {offset}) sbgames 
                left join favgames f on f.game_id = sbgames.row_id
            """
        else:
            q = f"""
                SELECT ag.* from all_games ag 
                order by ag.perc_discount DESC 
                limit {limit} offset {offset}
            """
        # list of dictoinary like objects
        return db.session.execute(text(q)).mappings().all()
    

    def shop_games(limit=20, offset=0, search=False, term=None):
        if search:
            q = f"""
                    SELECT * from (SELECT ag.* from all_games ag
                    where 1=1
                    and ag.name like '%{term}%' 
                    order by ag.perc_discount DESC ) sbgames 
                    left join favgames f on f.game_id = sbgames.row_id
                """
            return db.session.execute(text(q)).mappings().all()
        else:
            q = f"""
                    SELECT * from (SELECT ag.* from all_games ag 
                    order by ag.perc_discount DESC 
                    limit {limit} offset :offset) sbgames 
                    left join favgames f on f.game_id = sbgames.row_id
                """
            return db.session.execute(text(q), {'offset': offset}).mappings().all()

    
    def get_fav(game_id, user_id):
        q = f"""
        select * 
        from favgames fg 
        where fg.game_id = {game_id} and fg.user_id = {user_id} 
        limit 1
        """
        data = db.session.execute(text(q)).mappings().first()
        return data
    
    def del_fav(game_id, user_id):
        q = """
        delete from favgames where game_id = :game_id and user_id = :user_id
        """
        db.session.execute(text(q), {"game_id": game_id, "user_id": user_id})
        db.session.commit()
        pass

    def insert_fav(game_id, user_id):
        q = """
        insert into favgames (game_id, user_id) values
        (:game_id, :user_id)
        """
        db.session.execute(text(q), {"game_id": game_id, "user_id": user_id})
        db.session.commit()
        pass