from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class Meal(db.Model):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_diet: Mapped[bool] = mapped_column(Boolean, default=True)
    ate_at: Mapped[DateTime] = mapped_column(DateTime())
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    owner = db.relationship('User')

    def __init__(self, name: str, is_diet: bool, owner_id: int, ate_at,
                 description: str = None):
        super().__init__()

        self.name = name
        self.ate_at = ate_at
        self.description = description
        self.is_diet = is_diet
        self.owner_id = owner_id

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "is_diet": self.is_diet,
            "ate_at": self.ate_at
        }
