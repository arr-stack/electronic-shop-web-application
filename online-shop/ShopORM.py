from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    article: Mapped[str] = mapped_column('article')
    category: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    manufacturer: Mapped[str] = mapped_column('manufacturer')
    amount: Mapped[int] = mapped_column('amount')
    price: Mapped[float] = mapped_column('price')
    description: Mapped[int] = mapped_column(ForeignKey('items_descriptions.id'))

class ItemDesc(Base):
    __tablename__ = 'items_descriptions'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    description: Mapped[str] = mapped_column('description')

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    email: Mapped[str] = mapped_column('email')
    username: Mapped[str] = mapped_column('username')
    first_name: Mapped[str] = mapped_column('first_name')
    middle_name: Mapped[str] = mapped_column('middle_name')
    last_name: Mapped[str] = mapped_column('last_name')
    password: Mapped[str] = mapped_column('password')
    role: Mapped[str] = mapped_column('role')

class Orders(Base):
    __tablename__ = 'shop_orders'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    email: Mapped[str] = mapped_column('email')
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    order_items: Mapped[int] = mapped_column(ForeignKey("order_items.id"))

class OrderItem(Base):
    __tablename__ = 'order_items'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('shopOrder.id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column('id', primary_key=True)
    category: Mapped[str] = mapped_column('category')



