from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)

class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    article: Mapped[str] = mapped_column('article')
    type: Mapped[str] = mapped_column('type')
    manufacturer: Mapped[str] = mapped_column('manufacturer')
    amount: Mapped[int] = mapped_column('amount')
    price: Mapped[float] = mapped_column('price')
    description: Mapped[str] = mapped_column('description')

# class User(Base):
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column('id', primary_key=True)
#     email: Mapped[str] = mapped_column('email')
#     phone: Mapped[str] = mapped_column('phone')
#     username: Mapped[str] = mapped_column('username')
#     password: Mapped[str] = mapped_column('password')

class ShopOrder(Base):
    __tablename__ = 'shopOrders'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    phone: Mapped[str] = mapped_column('phone')
    email: Mapped[str] = mapped_column('email')
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))

# class ShopOrderItem(Base):
#     __tablename__ = 'shopOrderItems'
#     id: Mapped[int] = mapped_column('id', primary_key=True)
#     order_id: Mapped[int] = mapped_column(ForeignKey('shopOrder.id'))
#     item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))