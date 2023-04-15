from flask import Flask, request, jsonify
from node import RaftNode
import asyncio
import sys
import threading

api = Flask(__name__)

nodes = {
	"node1": {"ip": "127.0.0.1", "port": 8000},
	"node2": {"ip": "127.0.0.1", "port": 8001},
}

# # Create and start the nodes
# tasks = []
# for node_id in nodes:
# 	node = RaftNode(node_id, nodes)
# 	tasks.apiend(asyncio.create_task(node.run()))

# # Run the nodes' event loops
# await asyncio.gather(*tasks)
node_id = "node1"
#api.run(nodes[node_id]["ip"], port=nodes[node_id]["port"])
raft_node = RaftNode(node_id, nodes)
#raft_node.state = "candidate"

@api.route("/requestVote", methods = ["GET", "POST"])
def request_votes():
	if request.method == "POST":
		data= {
		"term": raft_node.current_term,
		"voteGranted": True
		}
		return data
	#data = (raft_node.request_vote())
	#print(data, file=sys.stderr)
	#voting_data = data[0]
	#response = data[1]
	return 200
	
@api.route("/apiendEntries", methods = ["POST", "GET"])
def apiendEntries():
	if request.method == "POST":
		data = {
		"term": raft_node.current_term,
		"success": True
		}
		raft_node.reset_timeout()
		return data
	#data = raft_node.send_heartbeats()
	#print(data, file=sys.stderr)
	#entry = data[0]
	#response = data[1]
	return 200

async def main():
	# Define the nodes
	await raft_node.run()
	
def run_flask():
	api.run(nodes[node_id]["ip"], port=nodes[node_id]["port"])

if __name__ == '__main__':
	flask_Thread = threading.Thread(target=run_flask)
	flask_Thread.start()

	while True:
		asyncio.run(main())
