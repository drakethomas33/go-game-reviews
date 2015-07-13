$('document').ready(function(){
    <!-- Activating a player using javascript -->
    var elem = document.getElementById("player");
    var player = new WGo.BasicPlayer(elem, {
        sgfFile: game_path
    });
});