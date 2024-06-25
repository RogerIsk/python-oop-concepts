from server_errors import OK, NotFound, ServerError

# Write code to test your classes

ok = OK(200)
not_found = NotFound(404)
server_error = ServerError(500)

for error in [ok, not_found, server_error]:
    error.status()