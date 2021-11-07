from high_lvl_networking import Server


server = Server(debug=False)
server.setup()
server.new_connection("id")

print(server.connections["id"])