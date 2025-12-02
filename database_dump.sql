--
-- PostgreSQL database dump
--

\restrict hPoFAkv8jJhRltbD7DVXmO0hLGdgzDarnzhda1GzZGvOffi1MZGshTdwBag8ccs

-- Dumped from database version 16.11
-- Dumped by pg_dump version 16.11

-- Started on 2025-12-02 00:54:20

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16406)
-- Name: reviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reviews (
    review_id text,
    bank character varying(50),
    app_name character varying(100),
    score integer,
    content text,
    at character varying(50),
    source character varying(50),
    sentiment_score double precision,
    sentiment_label character varying(20)
);


ALTER TABLE public.reviews OWNER TO postgres;

--
-- TOC entry 4877 (class 0 OID 16406)
-- Dependencies: 215
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reviews (review_id, bank, app_name, score, content, at, source, sentiment_score, sentiment_label) FROM stdin;
\.


-- Completed on 2025-12-02 00:54:20

--
-- PostgreSQL database dump complete
--

\unrestrict hPoFAkv8jJhRltbD7DVXmO0hLGdgzDarnzhda1GzZGvOffi1MZGshTdwBag8ccs

