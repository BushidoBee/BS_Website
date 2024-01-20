<?php
include 'dbconnection.php';
session_start();

$user_id = $_SESSION['user_id'];

if(isset($_POST['orders'])){
    $checkbox = $_POST['checkbox'];
    $order_id = $_POST['orders'];
    $fullname= "";
    $last_ids = [];
    $name = $_POST['name'];



    //alert($name);

    //Query the cashier's name to  be inserted to sales table
    $user_query = mysql_query("SELECT full_name FROM account WHERE acct_id = $user_id");
    while($row = mysql_fetch_array($user_query)){
        $fullname = $row['full_name'];
    }

    //insert orders into orders table
        $insert = mysql_query("INSERT INTO sales VALUES ('','$fullname',now(),$checkbox)");

        if($insert){
            $last_id = mysql_insert_id();
        }
    foreach($order_id as $key => $value) { //$key = dish_id and $value = quantity


        $dish_query = mysql_query("SELECT dish FROM menu WHERE menu_id = $key");
        while($dish = mysql_fetch_array($dish_query)){

            $dish = $dish['dish'];
            /*$name = $_POST['name'];*/
            $order = mysql_query("INSERT INTO orders VALUES ('', '$dish','$value','$last_id','$name')");

            $query1 = mysql_query("INSERT into a_logs(id,name,activity,a_date) values(0,'$fullname','Added $dish',NOW())");

            $recent_order_id = mysql_insert_id();

        }       
    }
}

?>