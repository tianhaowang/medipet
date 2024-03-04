CREATE TABLE `medicine` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NOT NULL,
  `recommended_dosage` TEXT NOT NULL,
  `image` TEXT,
  PRIMARY KEY (`id`)
);

CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `active` BOOLEAN,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`), -- Corrected the syntax for unique keys
  UNIQUE KEY (`email`),    -- Corrected the syntax for unique keys
  UNIQUE KEY (`phone`)     -- Corrected the syntax for unique keys
);

CREATE TABLE `schedule` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `medicine_id` INT NOT NULL,
  `time` VARCHAR(40) NOT NULL,
  `taken` BOOLEAN NOT NULL,
  `dosage` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
  FOREIGN KEY (`medicine_id`) REFERENCES `medicine`(`id`)
);

CREATE TABLE `doctor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `medical_license` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`), -- Corrected the syntax for unique keys
  UNIQUE KEY (`email`),    -- Corrected the syntax for unique keys
  UNIQUE KEY (`phone`)     -- Corrected the syntax for unique keys
);

CREATE TABLE `conditions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

-- patient
CREATE TABLE `doctor_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `doctor_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`doctor_id`) REFERENCES `doctor`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

-- illness
CREATE TABLE `user_condition` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `condition_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`condition_id`) REFERENCES `conditions`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

-- backend
CREATE TABLE `children` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Parent_id` INT, -- Added field for foreign key reference
  `Points` INT,
  `Hunger` INT,
  `Happiness` INT,
  `Health` INT,
  `Alert_threshold` INT,
  `Miss_threshold` INT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`Parent_id`) REFERENCES `users`(`id`) -- Foreign key constraint added
);

