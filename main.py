from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# https://www.youtube.com/watch?v=GMppyAPbLYk&list=PLHocQMwDsV-jp3z7T4ousLoTpaM_3uGBs&index=17&ab_channel=TechWithTim
    # NEXT 39:18 - Handling Delete Requests

app = Flask(__name__)
api = Api(app)

# validation
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video is required', required = True)
video_put_args.add_argument('views', type=int, help='Views of the video is required', required = True)
video_put_args.add_argument('likes', type=int, help='Likes on the video is required', required = True)

# main dbase
videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Video ID is not valid...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, '/video/<int:video_id>')


if __name__ == '__main__':
    app.run(debug=True)

