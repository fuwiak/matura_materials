tabele 
wyn: idw,idk,pkt
wys: idw,rok,miejsce
kier: idk, nazwa,imie,kraj

z1.
select *from wyn,kier,wys
where wyn.idk=kier.idk and wyn.idw=wys.idw
and nazw='Kubica' and imie = 'Robert'
order by pkt desc
//limit 1

z2.
select miejsce, count(*) ile from wys
group by miejsce
order by ile

z3.
select nazw,imie,sum(pkt) for wyn,kier,wys
where kier.idk=wyn.idk and wys.idw=wyn.idw
and rok = 2012 //2000, 2008
group by idk,nazw,imie
order by sum(pkt)

z4.
select kraj, count(*) from
(
select distinct kraj,idk from kier,wyn,wys
where kier.idk=wyn.idk and wys.idw=wyn.idw
and rok = 2012
)
group by kraj

