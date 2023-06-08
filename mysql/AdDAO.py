import random

from mysql.MySQLPool import MySQLPool


class AdDAO:

    @classmethod
    def get_ad(cls, to_user_name=""):
        rows = MySQLPool().execute_query("select a.front_content, a.aft_content from t_group g "
                                         "join t_ad_group ag on ag.group_id = g.id "
                                         "join t_ad a on a.id = ag.ad_id "
                                         "where g.name = %s", to_user_name)
        ad_item = {
            "front_content": "",
            "aft_content": ""
        }
        if len(rows) > 0:
            ad_item = random.choice(rows)
        return ad_item
