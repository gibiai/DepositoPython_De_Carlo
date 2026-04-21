-- inner join
select ordini.id, clienti.nome, ordini.data_ordine
from ordini
inner join clienti on ordini.id_cliente = cliente.id;

-- left join

insert into cliente(nome, città)
values ('Pippo', 'Topolinia');

select ordini.id, clienti.nome
from clienti
left join ordini
on clienti.id = ordini.id_cliente
order by clienti.nome;

-- cross join

select clienti.nome, ordini.id
from clienti
cross join ordini