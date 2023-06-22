use loja_peixes;
INSERT INTO peixes values (default, 'molinesio dalmata', 1);
INSERT INTO peixes values (default, 'acara_tigre', 2);
INSERT INTO peixes values (default, 'Guppy Neon', 3);
INSERT INTO peixes values (default, 'coridora_pimenta', 4);
INSERT INTO peixes values (default, 'betta_cauda_de_veu', 5);
INSERT INTO peixes values (default, 'peixe_tetra', 6);

INSERT INTO racas values (default, 'Guppy');
INSERT INTO racas values (default, 'coridora');
INSERT INTO racas values (default, 'Betta');
INSERT INTO racas values (default, '');
INSERT INTO racas values (default, 'Neon');
select * from peixes join racas on peixes.id;
select * from peixes;
select * from racas;

