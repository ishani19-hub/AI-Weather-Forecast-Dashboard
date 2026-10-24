def load_css():

    return """

<style>

/* Main Background */

.stApp {

    background:
    linear-gradient(
        135deg,
        #e3f2fd,
        #ffffff
    );

}


/* Main Title */

.title {

    text-align:center;

    font-size:48px;

    font-weight:800;

    color:#0077b6;

    margin-bottom:5px;

}


/* Subtitle */

.subtitle {

    text-align:center;

    font-size:20px;

    color:#555;

    margin-bottom:30px;

}



/* Glass Cards */

.card {


    background:
    rgba(255,255,255,0.75);


    backdrop-filter:
    blur(10px);


    padding:25px;


    border-radius:25px;


    box-shadow:

    0px 8px 30px
    rgba(0,0,0,0.12);


    border:
    1px solid rgba(255,255,255,0.3);


}



/* Forecast Cards */

.forecast-card {


    background:white;


    padding:20px;


    border-radius:20px;


    margin-bottom:20px;


    box-shadow:

    0px 5px 20px
    rgba(0,0,0,0.1);


    transition:
    transform 0.3s;


}



.forecast-card:hover {


    transform:
    translateY(-5px);


}




/* Buttons */


.stButton button {


    width:100%;


    height:50px;


    background:
    linear-gradient(
    90deg,
    #0077b6,
    #00b4d8
    );


    color:white;


    border:none;


    border-radius:15px;


    font-size:18px;


    font-weight:600;


}




.stButton button:hover {


    transform:
    scale(1.02);


}



/* Metrics */


[data-testid="stMetric"] {


    background:white;


    padding:15px;


    border-radius:15px;


    box-shadow:
    0px 4px 15px
    rgba(0,0,0,0.1);


}



/* Mobile Responsive */

@media(max-width:768px){


.title{

font-size:35px;

}


.subtitle{

font-size:16px;

}


}


</style>

"""