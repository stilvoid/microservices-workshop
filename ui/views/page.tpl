<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Babble</title>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

        <body>
            <nav class="navbar navbar-default">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a class="navbar-brand" href="#">Babble</a>
                    </div>
                </div>
            </nav>

            <div class="container-fluid">
                <div class="panel panel-primary">
                    <div class="panel-heading panel-title">
                        <span id="room-name">Babble: Choose a room</span>
                    </div>

                    <div class="panel-body">
                        <div class="row">
                            <div class="col-md-2">
                                <div class="panel panel-default">
                                    <div class="panel-heading panel-title">
                                        Rooms
                                    </div>

                                    <div class="panel-body">
                                        <div class="list-group" id="rooms"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-8">
                                <div class="panel panel-default">
                                    <div class="panel-body">
                                        <table class="table" id="chat">
                                        </table>

                                        <form class="form" id="chat-form">
                                            <input class="form-control" type="text" id="message" placeholder="New message" />
                                        </form>
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-2">
                                <div class="panel panel-default">
                                    <div class="panel-heading panel-title">
                                        Members
                                    </div>

                                    <div class="panel-body">
                                        <div class="list-group" id="members"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

        <script>
            var users = {};

            // Handle form submission
            $("#chat-form").submit(function() {
                post_message($("#message").val());

                $("#message").val("");

                return false;
            });

            function choose_room(room) {
                $("#members").html("");
                $("#chat").html("");

                $("#room-name").text(room.name + ": " + room.title);

                // Render members
                $.get("{{room}}/users").then(function(data) {
                    data.users.forEach(function(user) {
                        users[user.id] = user.name;
                    });

                    data.users.filter(function(user) {
                        return room.members.indexOf(user.id) !== -1;
                    }).forEach(function(user) {
                        $("#members").append(
                            $("<span>").addClass("list-group-item").text(user.name)
                        );
                    });
                });

                get_messages(room.id);
            }

            function get_rooms(callback) {
                $.get("{{room}}/rooms").then(function(data) {
                    data.rooms.forEach(function(room) {
                        var link = $("<a>").addClass("list-group-item").text(room.name);
                        link.append($("<span>").addClass("badge").text(room.members.length));
                        $("#rooms").append(link);
                        link.click(function() {
                            current_room = room.id;

                            $("#rooms a").removeClass("active");
                            link.addClass("active");
                            choose_room(room);
                            return false;
                        });
                    });

                    if(callback) {
                        callback();
                    }
                });
            }

            function get_messages(room_id) {
                $.get("{{message}}/messages?room=" + room_id).then(function(data) {
                    $("#chat").html("");

                    for(var i=Math.max(0, data.messages.length - 20); i<data.messages.length; i++) {
                        render_message(data.messages[i]);
                    }
                });
            }

            function render_message(message) {
                $("#chat").append(
                    $("<tr>").append(
                        $("<th>").text(users[message.user]),
                        $("<td>").html(message.text)
                    )
                );
            }

            function add_message(message) {
                $.ajax({
                    url: "{{message}}/messages",
                    contentType: "application/json",
                    method: "POST",
                    data: JSON.stringify(message)
                }).then(function() {
                    get_messages(message.room);
                });
            }

            function post_message(text) {
                var message = {
                    room: current_room,
                    user: current_user,
                    text: $("#message").val()
                };

                add_message(message);
            }

            var current_user = 0;
            var current_room = null;

            get_rooms(function() {
                $("#rooms a:first-child").click();

                setInterval(function() {
                    get_messages(current_room);
                }, 1000);
            });
        </script>
</html>
