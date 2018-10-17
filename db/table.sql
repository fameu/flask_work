use db_zqq;

--角色
create table role(
    id integer primary key,
    name text not null
);

--公司
create table company(
    id integer primary key,
    name text not null
);

--产品
create table product(
    id integer primary key,
    name text not null,
    info text
);


--出库记录
create table stock_out (
    id integer primary key,
    stm datetime,
    rid integer,
    cid integer,
    pid integer,
    cnt integer,
    foreign key (rid) references role(id),
    foreign key (cid) references company(id),
    foreign key (pid) references product(id)
);


--入库记录
create table stock_in (
    id integer primary key,
    stm datetime,
    rid integer,
    cid integer,
    pid integer,
    cnt integer,
    foreign key (rid) references role(id),
    foreign key (cid) references company(id),
    foreign key (pid) references product(id)
);