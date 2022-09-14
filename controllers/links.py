
from flask import Blueprint, jsonify, request, redirect
from models.links import LinkModel
from random import randint, randrange

from http import HTTPStatus
from app import db

from serializers.links import LinkSchema

from marshmallow.exceptions import ValidationError

#Creates route
router = Blueprint("links", __name__)
link_schema = LinkSchema()

@router.route("/links", methods=["GET"])
def get_all_links():

    text = f"SELECT * FROM links ORDER BY created_at DESC"
    print(text)
    try:
        records = db.engine.execute(text)

        if not records:
            return { "message": "No records found"}, HTTPStatus.OK

        results_list = [] 
        for r in records:
            r_dict = dict(r.items())
            print(r_dict)
            results_list.append(r_dict)

        return jsonify(results_list), HTTPStatus.OK

    except Exception as e:

        return {"messages" : "Something went wrong"}



@router.route("/<int:link_id>", methods=["GET"])
def get_specific_link(link_id):

    text = f"SELECT * FROM links WHERE links.short = {link_id}"
    print(text)
    try:
        records = db.engine.execute(text)

        if not records:
            return {"message": "shortened url does not exist"}, HTTPStatus.NOT_FOUND

        results_list = [] 
        for r in records:
            r_dict = dict(r.items())
            print(r_dict)
            results_list.append(r_dict)
        
        url =  results_list[0]['full']
        print(url)

        return url

    except Exception as e:

        return {"messages" : "Something went wrong"}

        

@router.route("/links", methods=["POST"])
def post_new_link():

    link_dictionary = request.json

    try:
        link = link_schema.load(link_dictionary)
    
    except ValidationError as e:
        return { "errors": e.messages, "message": "something went wrong" }

    while True:

        shortNum = randint(100000, 999999)
        existingLink = LinkModel.query.filter_by(short=shortNum).first()

        try: 
            if existingLink == None:
                link.short = shortNum

            else:
                continue

            link.save()
            return link_schema.jsonify(link), HTTPStatus.CREATED

        except ValidationError as e:

            return { "errors": e.messages, "message": "no numbers left" }



@router.route("/<int:link_id>", methods=["DELETE"])
def delete_link(link_id):

    print(link_id)

    existing_link = LinkModel.query.filter_by(short=link_id).first()

    if not existing_link:
      return {"message": "shortened url does not exist"}, HTTPStatus.NOT_FOUND

    try:
        existing_link.remove()

    except ValidationError as e:

        return {"errors:": e.messages, "messages": "Something went wrong"}

    return link_schema.jsonify(existing_link), HTTPStatus.OK


@router.route("/<int:link_id>", methods=["PUT"])
def update_link(link_id):
    link_dictionary = request.json
    existing_link = LinkModel.query.filter_by(short=link_id).first()

    if not existing_link:
      return {"message": "link not found"}, HTTPStatus.NOT_FOUND

      
    try:
        existing_link.full = link_dictionary['full']
        existing_link.save()


    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }

    return link_schema.jsonify(existing_link), HTTPStatus.OK



@router.route("/clicks/<int:link_id>", methods=["PUT"])
def update_click(link_id):
    link_dictionary = request.json
    existing_link = LinkModel.query.filter_by(short=link_id).first()

    if not existing_link:
      return {"message": "link not found"}, HTTPStatus.NOT_FOUND

      
    try:
        existing_link.clicks = existing_link.clicks + 1
        existing_link.save()


    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }

    return link_schema.jsonify(existing_link), HTTPStatus.OK
