-- Migracja 001: poszerzenie identyfikatorów przewodów/miejsc i brakujące klucze obce.
-- NIE jest uruchamiana automatycznie. Przed wykonaniem zrób kopię bazy:
--   mysqldump kb_ster > kb_ster_backup.sql
--
-- Powód: przewod.id i miejsce.id to TINYINT UNSIGNED (max 255),
-- a w bazie jest już ok. 218 przewodów i 109 miejsc.

ALTER TABLE `przewod_miejsce` DROP FOREIGN KEY `pmmiefg`, DROP FOREIGN KEY `pmprzefg`;
ALTER TABLE `zyla`            DROP FOREIGN KEY `zyla_przfk_2`;
ALTER TABLE `plytki`          DROP FOREIGN KEY `plytkimiejfg1`;

ALTER TABLE `przewod`         MODIFY `id`          SMALLINT UNSIGNED NOT NULL;
ALTER TABLE `miejsce`         MODIFY `id`          SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT;
ALTER TABLE `przewod_miejsce` MODIFY `przewod_id`  SMALLINT UNSIGNED NOT NULL,
                              MODIFY `miejsce_id`  SMALLINT UNSIGNED NOT NULL;
ALTER TABLE `zyla`            MODIFY `przewod_id`  SMALLINT UNSIGNED NOT NULL;
ALTER TABLE `plytki`          MODIFY `miejsce_id`  SMALLINT UNSIGNED NOT NULL;

ALTER TABLE `przewod_miejsce`
    ADD CONSTRAINT `pmmiefg`  FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`),
    ADD CONSTRAINT `pmprzefg` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`);
ALTER TABLE `zyla`
    ADD CONSTRAINT `zyla_przfk_2` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`);
ALTER TABLE `plytki`
    ADD CONSTRAINT `plytkimiejfg1` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`);

-- Osierocone rekordy blokują dodanie kluczy obcych. Najpierw je obejrzyj:
SELECT zz.* FROM `zakonczenie_zyly` zz
LEFT JOIN `zakonczenie` z ON z.id = zz.zakonczenie_id
LEFT JOIN `zyla` zy ON zy.id = zz.zyla_id
WHERE z.id IS NULL OR zy.id IS NULL;

-- ...a jeśli są zbędne, usuń (wskazują na nieistniejące zakończenia/żyły):
DELETE zz FROM `zakonczenie_zyly` zz
LEFT JOIN `zakonczenie` z ON z.id = zz.zakonczenie_id
LEFT JOIN `zyla` zy ON zy.id = zz.zyla_id
WHERE z.id IS NULL OR zy.id IS NULL;

ALTER TABLE `zakonczenie_zyly`
    ADD CONSTRAINT `zakzyl_zak_fk` FOREIGN KEY (`zakonczenie_id`) REFERENCES `zakonczenie` (`id`),
    ADD CONSTRAINT `zakzyl_zyla_fk` FOREIGN KEY (`zyla_id`) REFERENCES `zyla` (`id`);

ALTER TABLE `polaczenie_zyla`
    ADD CONSTRAINT `polzyla_zakzyl_fk` FOREIGN KEY (`zakonczenie_zyly_id`) REFERENCES `zakonczenie_zyly` (`id`);
