from flask import Blueprint, request, jsonify
from models import db, User, Job
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()
    if user:
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered"})


@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": token})


@routes.route("/jobs", methods=["POST"])
@jwt_required()
def add_job():
    user_id = get_jwt_identity()
    data = request.get_json()

    job = Job(
        company=data["company"],
        role=data["role"],
        status=data.get("status", "Applied"),
        user_id=user_id
    )

    db.session.add(job)
    db.session.commit()

    return jsonify({"msg": "Job added"})


@routes.route("/jobs", methods=["GET"])
@jwt_required()
def get_jobs():
    user_id = get_jwt_identity()

    jobs = Job.query.filter_by(user_id=user_id).all()

    result = []
    for job in jobs:
        result.append({
            "id": job.id,
            "company": job.company,
            "role": job.role,
            "status": job.status
        })

    return jsonify(result)


@routes.route("/jobs/<int:id>", methods=["PUT"])
@jwt_required()
def update_job(id):
    user_id = get_jwt_identity()
    job = Job.query.filter_by(id=id, user_id=user_id).first()

    if not job:
        return jsonify({"msg": "Job not found"}), 404

    data = request.get_json()

    job.company = data.get("company", job.company)
    job.role = data.get("role", job.role)
    job.status = data.get("status", job.status)

    db.session.commit()

    return jsonify({"msg": "Job updated"})


@routes.route("/jobs/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_job(id):
    user_id = get_jwt_identity()
    job = Job.query.filter_by(id=id, user_id=user_id).first()

    if not job:
        return jsonify({"msg": "Job not found"}), 404

    db.session.delete(job)
    db.session.commit()

    return jsonify({"msg": "Job deleted"})

@routes.route("/jobs/search", methods=["GET"])
@jwt_required()
def search_jobs():
    user_id = get_jwt_identity()

    company = request.args.get("company")
    status = request.args.get("status")

    query = Job.query.filter_by(user_id=user_id)

    if company:
        query = query.filter(Job.company.contains(company))

    if status:
        query = query.filter_by(status=status)

    jobs = query.all()

    return jsonify([
        {
            "id": job.id,
            "company": job.company,
            "role": job.role,
            "status": job.status
        }
        for job in jobs
    ])