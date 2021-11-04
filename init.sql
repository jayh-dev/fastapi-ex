CREATE DATABASE jfe;
\c jfe;
CREATE EXTENSION pgcrypto;
CREATE USER jfe WITH ENCRYPTED PASSWORD 'jfe';
GRANT ALL PRIVILEGES ON DATABASE jfe TO jfe;

\c jfe jfe;
--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6
-- Dumped by pg_dump version 12.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: item; Type: TABLE; Schema: public; Owner: jfe
--

CREATE TABLE public.item (
    id bigint NOT NULL,
    name character varying(128) NOT NULL,
    description character varying(256) DEFAULT ''::character varying,
    created timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.item OWNER TO jfe;

--
-- Name: TABLE item; Type: COMMENT; Schema: public; Owner: jfe
--

COMMENT ON TABLE public.item IS 'Item';


--
-- Name: COLUMN item.id; Type: COMMENT; Schema: public; Owner: jfe
--

COMMENT ON COLUMN public.item.id IS 'Database ID';


--
-- Name: COLUMN item.name; Type: COMMENT; Schema: public; Owner: jfe
--

COMMENT ON COLUMN public.item.name IS 'Name';


--
-- Name: COLUMN item.description; Type: COMMENT; Schema: public; Owner: jfe
--

COMMENT ON COLUMN public.item.description IS 'Description';


--
-- Name: COLUMN item.created; Type: COMMENT; Schema: public; Owner: jfe
--

COMMENT ON COLUMN public.item.created IS 'Created Timestamp';


--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: jfe
--

CREATE SEQUENCE public.item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO jfe;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jfe
--

ALTER SEQUENCE public.item_id_seq OWNED BY public.item.id;


--
-- Name: item id; Type: DEFAULT; Schema: public; Owner: jfe
--

ALTER TABLE ONLY public.item ALTER COLUMN id SET DEFAULT nextval('public.item_id_seq'::regclass);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: jfe
--

COPY public.item (id, name, description, created) FROM stdin;
1	Item01	Item01 Description	2021-10-28 14:33:10.000000
2	Item02	Item02 Description	2021-10-28 14:33:11.000000
3	Item03	Item03 Description	2021-10-28 14:33:12.000000
4	Item04	Item04 Description	2021-10-28 14:33:13.000000
5	Item05	Item05 Description	2021-10-28 14:33:14.000000
6	Item06	Item06 Description	2021-10-28 14:33:15.000000
7	Item07	Item07 Description	2021-10-28 14:33:16.000000
8	Item08	Item08 Description	2021-10-28 14:33:17.000000
9	Item09	Item09 Description	2021-10-28 14:33:18.000000
10	Item10	Item10 Description	2021-10-28 14:33:19.000000
11	Item11	Item11 Description	2021-10-28 14:33:20.000000
12	Item12	Item12 Description	2021-10-28 14:33:21.000000
13	Item13	Item13 Description	2021-10-28 14:33:22.000000
14	Item14	Item14 Description	2021-10-28 14:33:23.000000
15	Item15	Item15 Description	2021-10-28 14:33:24.000000
16	Item16	Item16 Description	2021-10-28 14:33:25.000000
17	Item17	Item17 Description	2021-10-28 14:33:26.000000
18	Item18	Item18 Description	2021-10-28 14:33:27.000000
19	Item19	Item19 Description	2021-10-28 14:33:28.000000
20	Item20	Item20 Description	2021-10-28 14:33:29.000000
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jfe
--

SELECT pg_catalog.setval('public.item_id_seq', 20, true);


--
-- Name: item item_name_key; Type: CONSTRAINT; Schema: public; Owner: jfe
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_name_key UNIQUE (name);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: jfe
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

