from github import Github
from flask import Flask
from flask import jsonify
import sys
import yaml
import json
from github import RateLimitExceededException
from github import UnknownObjectException

app = Flask(__name__)
githubUrl = sys.argv[1].split('/')
    
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    for index in range(len(githubUrl)) :
        if "github.com" in githubUrl[index] :
            username = githubUrl[index+1]
            repositoryName = githubUrl[index+2]
        else :
            output = "Not a valid github repository"
    
    input = path.split('/')
    
    try:
		repository = Github().get_user(username).get_repo(repositoryName)
    except RateLimitExceededException:
		output = "Please try again after sometime."
    except Exception:
		output = "Invalid repository/user"
    
    try :
		for i in range(len(input)):
			if ".yml" in input[i] :
				config_file = input[i]
				output=jsonify(yaml.safe_load(repository.get_file_contents(config_file).content.decode(repository.get_file_contents(config_file).encoding)))
			elif ".json" in input[i] :
				config_file = input[i]
				output=jsonify(json.loads(repository.get_file_contents(config_file).content.decode(repository.get_file_contents(config_file).encoding)))
			else : 
				output = "Invalid file format"
                
    except UnknownObjectException :
		output = "File not found in the repository"    

    return output

if __name__ == "__main__":
    app.config["githubUrl"] = sys.argv[1]
    app.run(debug=True,host='0.0.0.0')