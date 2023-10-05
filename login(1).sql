-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 05/10/2023 às 14:06
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `login`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `email` varchar(40) NOT NULL,
  `senha` varchar(100) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`email`, `senha`, `id`) VALUES
('wagner-crz@hotmail.com', '$2y$10$0XG1PGsp9qt/6qeigoTzWuZuVrzrGka0/BqH1hudVLE06H2hoNhIe', 3),
('brenobastos11-crz@outlook.com', '$2y$10$cfF8TH6e2Xc.iHHkgJk.4.pnJSTr86CPU/zyT.44WS0HM9BsvNZOS', 5),
('brenobastos11-crz@outlook.com.br', '$2y$10$rUjr/5NgBfh018Kbs9U4EebrYHaIV2IGdoG89GzMGDY5hvPGZqwEq', 6),
('vanderlei@outlook.com', '$2y$10$XgzyqBsuBgCHX1s5Lj6zXu6sjydwHaWkUcg0Qn6gEnSmAExmgyzLS', 7),
('brenobastos11-crz@gmail.com.br', '$2y$10$6c7XWOE704OqJw0ppLlhSO6QLK9et3YU53OKX0WpGOxQ.VdOKN2Ja', 8),
('vhpj@outlook.com', '$2y$10$SACUDazxiRbbizMBFdWrnedqOBDctGaD.ReXEmDXXtbfYeSGU6tES', 9),
('vhpj@hotmail.com', '$2y$10$cbO3tiU5.kVruxpTvsVT5OjKjWuyoHFAq6J.mjXleShylwIcDKAye', 10),
('vanderlei@outlook.com.br', '$2y$10$NIPRNNxwHh7z532tpxlIAueatRc0mk2KBKSySxwGrwxRQEnToodJ2', 11),
('wagnersilva@outlook.com.br', '$2y$10$FwyLKtrk2GME6ryQ2ITOD.SjXerpgIu28jdRSxu.LLZ7r0CjFP.wm', 12);

-- --------------------------------------------------------

--
-- Estrutura para tabela `videos`
--

CREATE TABLE `videos` (
  `email` varchar(100) NOT NULL,
  `id` int(11) NOT NULL,
  `video_url` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `videos`
--

INSERT INTO `videos` (`email`, `id`, `video_url`) VALUES
('brenobastos11-crz@outlook.com', 36, 'video-650c41c5173e26.20013829.mp4'),
('brenobastos11-crz@outlook.com', 37, 'video-651b2424e7ee58.25018382.mp4'),
('brenobastos11-crz@outlook.com', 38, 'video-651b2602987bf8.96622783.mp4'),
('brenobastos11-crz@outlook.com', 39, 'video-651c0a06b1d922.36689626.mp4'),
('brenobastos11-crz@gmail.com.br', 40, 'video-651c7604d89e50.02550786.mp4'),
('brenobastos11-crz@gmail.com.br', 41, 'video-651c76bc8f00b3.92958948.mp4'),
('brenobastos11-crz@outlook.com', 42, 'video-651ea5017dcf17.60075038.mp4'),
('brenobastos11-crz@outlook.com', 43, 'video-651ea59a7d6425.22065616.mp4');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
