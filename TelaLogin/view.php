
<?php
session_start();
if (isset($_POST['upload']) && isset($_FILES['video'])) {
    include "config.php";
    $video_nome = $_FILES['video']['name'];
    $tmp_nome = $_FILES['video']['tmp_name'];
    $error = $_FILES['video']['error'];

    if ($error == 0) {
        $video_ex = pathinfo($video_nome, PATHINFO_EXTENSION);
        $video_ex_lc = strtolower($video_ex);
        $allowed_exs = array("mp4", "webm", "avi", "flv");

        if (in_array($video_ex_lc, $allowed_exs)) {
            $new_video_nome = uniqid("video-", true) . '.' . $video_ex_lc;
            $video_upload_path = 'uploads/' . $new_video_nome;
            move_uploaded_file($tmp_nome, $video_upload_path);

            if (isset($_SESSION['user_email'])) {
                $email = $_SESSION['user_email'];
                $sql = "INSERT INTO videos (email, video_url) VALUES ('$email', '$new_video_nome')";
                mysqli_query($conn, $sql);
                header("Location: indexVideo.php");
                exit;
            } else {
                $em = "Erro: Usuário não autenticado.";
                header("Location: Video.php?error=$em");
                exit;
            }
            
        } else {
            $em = "Erro: Formato inválido.";
            header("Location: Video.php?error=$em");
            exit;
        }
    } else {
        $em = "Erro: Nenhum arquivo selecionado.";
        header("Location: Video.php?error=$em");
        exit;
    }
} else {
    $em = "Erro: Nenhum arquivo selecionado.";
    header("Location: Video.php?error=$em");
    exit;
}
?>



