var imgNumber = 0;
    var NumberOfId = 8-1;
    var idName = new Array(NumberOfId);
    idName[0] = "myAudio1";
    idName[1] = "myAudio2";
    idName[2] = "myAudio3";
    idName[3] = "myAudio4";
    idName[4] = "myAudio5";
    idName[5] = "myAudio6";
    idName[6] = "myAudio7";
    idName[7] = "myAudio8";
    idName[8] = "myAudio9";
    idName[9] = "myAudio10";
    idName[10] = "myAudio11";
    idName[11] = "myAudio12";



    


    function play_pause(i) {
            
            var myAudio = document.getElementById(idName[i]);
            if (myAudio.paused) {
                myAudio.play();
            } else {
                myAudio.pause();
            }

            
        }