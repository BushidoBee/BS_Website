<?php
include 'RLBooksDB.php';
session_start();

$user_id = $_SESSION['user_id'];

if(isset($_POST['Rentals'])){
    $rent_pack = $_POST['rental'];
    $cus_name = $_POST['name'];
    $location = $_POST['location'];
    $phone_num = $_POST['phone'];
    alert("New Order for: ", $cus_name, "(",$user_id,")");

    //Query the Rental Order to be inserted to Active Booking List
    $user_query = mysql_query("SELECT ord_id, rent_pack, cus_name FROM Rentals WHERE rent_id = $user_id");
    while($row = mysql_fetch_array($user_query))
    {
        $ord_id = $row['rental'];
    }

    //insert current rental into the Rentals table
    $new_insert = mysql_query("INSERT INTO Rentals VALUES ($user_id,$rent_pack,'$cus_name',$location,$phone_num)");

        if($new_insert)
        {
            $ord_id = mysql_insert_id();
        }
        
        // Bookmark: still editing file up to this point
        foreach($order_id as $key => $value) { //$key = dish_id and $value = quantity


        $dish_query = mysql_query("SELECT dish FROM menu WHERE menu_id = $key");
        while($dish = mysql_fetch_array($dish_query)){

            $dish = $dish['dish'];
            /*$name = $_POST['name'];*/
            $order = mysql_query("INSERT INTO Rentals VALUES ('', '$dish','$value','$last_id','$name')");

            $query1 = mysql_query("INSERT into a_logs(id,name,activity,a_date) values(0,'$fullname','Added $dish',NOW())");

            $recent_order_id = mysql_insert_id();

        }       
    }
}

?>