

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SampleOperationsCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "SampleOperations" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_input TEXT NOT NULL, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_input) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(has_output) REFERENCES "NamedThing" (id)
);
