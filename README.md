# REST_API
a basic RESTFULL API with flask and mongdb (CRUD)

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
          integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title>help</title>
</head>
<body>
<div class="container">
    <!-- Content here -->

    <div class="alert alert-primary w-10 p-2" role="alert">
        <center><h1 style="color:blue">Welcome to my First API with Flask</h1></center>
    </div>
    <div class="container w-2 p-5">
        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /insert / int:id / string:name / string:adresse </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /delete_all </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /select_all </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /select_first </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /find_by_adr / string:adresse </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /find_by_name/ string:name </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /sort_by_adr </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /sort_by_name/ </h5></center>
        </div>


        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /sort_by_id/ </h5></center>
        </div>

        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /update_name/int:id/old_name/new_name </h5></center>
        </div>


        <div class="alert alert-success w-5 p-1" role="alert">
            <center><h5 style="color:green"> /update_adr/int:id/old_adr/new_adr </h5></center>
        </div>
    </div>

</div>


<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
        integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
        integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
        crossorigin="anonymous"></script>
</body>
</html>