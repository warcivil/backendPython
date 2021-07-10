from models import User, LoveRGBColor, WorkInfo, session, engine
from sqlalchemy import func, update
from exception_handler import exception_handler
import sqlalchemy


class UserController():
    @staticmethod
    @exception_handler
    def create(name: str, full_name: str, password: str, color: str,
               work_company: str, post: str) -> User:

        user = User(
            name=name,
            fullname=full_name,
            password=password,
        )
        next_user_id = list(session.query(func.Max(User.id))[0])[0] + 1

        work_info = WorkInfo(work_company=work_company,
                             post=post,
                             user_id=next_user_id)
        love_rgb_color = LoveRGBColor(color=color, user_id=next_user_id)
        session.add(user)
        session.add(work_info)
        session.add(love_rgb_color)
        session.commit()
        return user

    @staticmethod
    @exception_handler
    def read(user_id) -> sqlalchemy.orm.query.Query:
        query = session.query(
            User.name, User.fullname, User.password, LoveRGBColor.color,
            WorkInfo.work_company,
            WorkInfo.post).where(User.id == user_id).join(LoveRGBColor).filter(
                LoveRGBColor.user_id == User.id).join(WorkInfo).filter(
                    WorkInfo.user_id == User.id)
        return query

    @staticmethod
    @exception_handler
    def update(user_id: int, name: str, fullname: str, password: str,
               color: str, work_company: str, post: str):
        conn = engine.connect()

        update_user = (update(User).where(User.id == user_id).values(
            name=name, fullname=fullname, password=password))
        update_color = (update(LoveRGBColor).where(
            LoveRGBColor.user_id == user_id).values(color=color))
        update_work_company = (update(WorkInfo).where(
            WorkInfo.user_id == user_id).values(post=post,
                                                work_company=work_company))
        conn.execute(update_user)
        conn.execute(update_color)
        conn.execute(update_work_company)

    @staticmethod
    @exception_handler
    def delete(user_id: int):
        session.query(User).filter_by(id=user_id).delete()
        session.query(LoveRGBColor).filter_by(user_id=user_id).delete()
        session.query(WorkInfo).filter_by(user_id=user_id).delete()
        session.commit()

    @staticmethod
    @exception_handler
    def get_all() -> sqlalchemy.orm.query.Query:
        query = session.query(
            User.name, LoveRGBColor.color, WorkInfo.work_company,
            WorkInfo.post).join(LoveRGBColor).filter(
                LoveRGBColor.user_id == User.id).join(WorkInfo).filter(
                    WorkInfo.user_id == User.id)
        return query