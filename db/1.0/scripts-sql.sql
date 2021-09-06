-- Departamento
CREATE TABLE Departamento
(
    id_departamento int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(160) NOT NULL.
    CONSTRAINT departamento_pk PRIMARY KEY (id_departamento)
);


-- Colaborador

CREATE TABLE Colaborador
(
    id_colaborador int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(160)  NOT NULL,
    id_departamento INTEGER  NOT NULL,
    CONSTRAINT colaborador_pk PRIMARY KEY (id_colaborador)
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);


-- Dependente

CREATE TABLE Dependente
(
    id_dependente int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
    nome NVARCHAR(160)  NOT NULL,
    id_colaborador INTEGER  NOT NULL,
    CONSTRAINT dependente_pk PRIMARY KEY (id_dependente)
    FOREIGN KEY (id_colaborador) REFERENCES Colaborador (id_colaborador) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);