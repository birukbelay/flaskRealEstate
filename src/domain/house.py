from src import db
from src.models.houses import House
from src.utils.result import Result


def create_house(house_dict):
    try:
        house=House(**house_dict)
        db.session.add(house)
        db.session.commit()
        return Result.Ok(house.__repr__())
    except Exception as e:
        return Result.Fail(e.args)


def get_allHouse():
    try:
        houses = House.query.all()
        return Result.Ok(houses)
    except Exception as e:
        return Result.Fail(e.args)



def delete_house(id):
    try:
        house = House.query.get_or_404(id)
        if not house:
            return Result.Fail("no house by this id")
        db.session.delete(house)
        db.session.commit()
        return Result.Ok("house deleted")
    except Exception as e:
        return Result.Fail(e.args)


def get_one_house(id):
    try:
        house = House.query.get_or_404(id)
        return Result.Ok(house)
    except Exception as e:
        return Result.Fail(e.args)


def update_house(id, house_dict):
    try:
        house = House.query.get_or_404(id)
        if not house:
            return Result.Fail("no house by this id")
        for k, v in house_dict.items():
            setattr(house, k, v)
        db.session.commit()
        message = f"'{id}' was successfully updated"
        return Result.Ok(message)
    except Exception as e:
        return Result.Fail(e)
def search_house(searchstring):
    try:
        house = House.query.get_or_404(searchstring)
        if not house:
            return Result.Fail("no house by this name")
        house = House.filter(House.description.like('%'+searchstring+'%'))
        houses = house.order_by(House.description).all()
        return Result.ok(houses)
    except Exception as e:
        return Result.Fail(e)

