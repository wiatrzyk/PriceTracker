from app import app, db
from flask import render_template, redirect, url_for
from app.scraper import check_price, find_image
from app.forms import ItemForm
from app.models import Item
import re


@app.route("/home")
def hello():
    return "Hello World!"

@app.route("/", methods=['GET', 'POST'])
def home():
    items = Item.query.all()
    for item in items:
        price = check_price(item.url)
        if price is not None:
            cleaned_price = re.search(r"\d+[,.]\d+", price).group()
            item.newest_price = cleaned_price.replace(",",".")
            db.session.commit()
    return render_template("tracker.html", items=items)

@app.route("/new_tracker", methods=['GET', 'POST'])
def add_tracker():
    form = ItemForm()
    if form.validate_on_submit():
        price = check_price(form.data['url'])
        if price is not None:
            cleaned_price = re.search(r"\d+[,.]\d+", price).group().replace(",",".")
            image_url = find_image(form.data['url'])
            new_item = Item(name=form.data['name'], url=form.data['url'], 
                            original_price = cleaned_price, image_url=image_url)
            db.session.add(new_item)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_tracker.html', title='Add item', form=form)

@app.route("/item/delete/<int:item_id>", methods=['POST'])
def delete_item(item_id):
    Item.query.filter(Item.id == item_id).delete()
    db.session.commit()
    return redirect(url_for('home'))
