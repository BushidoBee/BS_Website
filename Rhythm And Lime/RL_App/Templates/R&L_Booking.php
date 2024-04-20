<?php
// include 'RLBooksDB.php';
session_start();

$user_id = $_SESSION['user_id'];

if(isset($_POST['Rentals'])){
    $rent_pack = $_POST['Rentals'];
    $cus_name = $_POST['name'];
    $location = $_POST['location'];
    $phone_num = $_POST['phone'];
    alert("New Order for: ", $cus_name, " - (",$user_id,")");

//Query the Rental Order to be inserted to Active Booking List
$user_query = mysql_query("SELECT rent_id, rent_pack, cus_name FROM Rentals WHERE rent_id = $user_id");
while($row = mysql_fetch_array($user_query))
{
 $ord_id = $row['rent_id'];
}

//insert current rental into the Rentals table
$new_insert = mysql_query("INSERT INTO Rentals VALUES ($user_id,$rent_pack,'$cus_name',$location,$phone_num)");

if($new_insert){
  $ord_id = mysql_insert_id();
}
foreach($order_id as $key => $value)// Bookmark: still editing file up to this point 
{ //$key = dish_id and $value = quantity

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

<form action="reserve_a_margarita_machine_online.cfm" method="post" name="rfrm">
	<input type="hidden" name="formkey" value="reservations" /><fieldset id="reservescreen">
	<legend>Reserve a Rental</legend>
	<table border="0" cellpadding="2" cellspacing="0" id="resform" summary="Reserve your Margarita Machine today."><tr>

        <th scope="row">Your Name:</th><td><input name="customer_name" type="text" id="customer_name" size="55" /></td></tr>

        <tr><th scope="row">Delivery Address:</th><td><input name="custAddress" type="text" id="custAddress" size="55" /></td></tr><tr>

        <th scope="row">Zip Code:</th><td><input name="custzip" type="text" id="custzip" size="25" /></td></tr>

        <tr><th scope="row">Day Phone:</th><td><input name="dayphone" type="text" id="dayphone" /></td></tr><tr>

        <th scope="row"><p>Evening Phone:</p></th><td><input name="nightphone" type="text" id="nightphone" /></td></tr><tr>
        
        <th scope="row">Email Address:</th><td><input name="custemail" type="text" id="custemail" size="55" /></td></tr><tr>
        <td colspan="2" scope="row">&nbsp;</th>
            </tr><tr>
        <th nowrap="nowrap" scope="row">How Many Guests?</th><td>
            <select name="numGuests" id="numGuests">
                <option value="Undecided" selected="selected">Not Sure</option>
                <option value="<25">1 - 25</option>
                <option value="<50">25 - 50</option>
                <option value="<75">50 - 75</option>
                <option value="<100">75 - 100</option>
                <option value="<150">100 - 150</option>
                <option value="<200">150 - 200</option>
                <option value="200+">200+</option>
            </select></td></tr>
        <tr><th scope="row"> Party Date:</th><td><input name="partydt" type="text" id="partydt" size="15" /></td></tr>

        <tr><th scope="row">Party Time:</th><td><select name="partytime" id="partytime">
            <option value="1:00">1:00</option>
            <option value="2:00">2:00</option>
            <option value="3:00">3:00</option>
            <option value="4:00">4:00</option>
            <option value="5:00">5:00</option>
            <option value="6:00">6:00</option>
            <option value="7:00">7:00</option>
            <option value="8:00">8:00</option>
            <option value="9:00">9:00</option>
            <option value="10:00">10:00</option>
            <option value="11:00">11:00</option>
            <option value="12:00">12:00</option>
            </select>&nbsp;&nbsp;
            <input name="ampm" type="radio" value="am" />AM
            <input name="ampm" type="radio" value="pm" checked="checked" />PM</td>
            </tr>
        <tr><th scope="row">&nbsp;</th><td>&nbsp;</td></tr>

        <tr><th colspan="2" style="color:#007832;" scope="row">How can we help?</th></tr>

        <tr><th scope="row">Machine Type:</th><td><input name="machinetype" type="radio" value="single" />Single &nbsp; 
        <input name="machinetype" type="radio" value="???" checked="checked" />Not Sure </td></tr>

        <tr><th scope="row" valign="top">Mix Flavor(s):</th>
            <td><div class="colx2"><input name="flavor" type="checkbox" value="Blue Raspberry" /> Blue Raspberry</div>
            <div class="colx2"><input name="flavor" type="checkbox" value="Lemonade" /> Lemonade</div>
            <div class="colx2"><input name="flavor" type="checkbox" value="Louisiana Hurricane" /> Louisiana Hurricane</div>
            <div class="colx2"><input name="flavor" type="checkbox" value="Margarita" /> Margarita</div>
            <div class="colx2"><input name="flavor" type="checkbox" value="Pina Colada" /> Pina Colada</div>
            <div class="colx2"><input name="flavor" type="checkbox" value="Strawberry" /> Strawberry</div></td>
        </tr>
        <tr><th colspan="2" scope="row">Any Other information?</th></tr><tr>
        <th colspan="2" scope="row"><textarea name="comments" cols="60" rows="3" wrap="VIRTUAL" id="comments"></textarea></th>
            </tr>
                <tr class="hotshot">
        <th scope="row">6 + 5</th>
        <td colspan="2" align="center"><input type="text" value="" name="humancheck" /></td></tr>
        <tr><td colspan="2" align="center"><input type="submit" value="Reserve" name="Reservation" /></td></tr>
    </table>
	</fieldset></form>