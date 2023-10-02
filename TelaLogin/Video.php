<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php if(isset($_GET['error'])){
?>
<p><?=$_GET['error']?></p>
   <?php }?>
    <form action="view.php" method= "POST" enctype="multipart/form-data">
    <input type="file" name="video">
    <input type="submit" name="upload" value="upload">
    <button type="button" onclick="window.location.href = 'TelaVideo.php';">Voltar </button> 
    </form>
</body>
</html>