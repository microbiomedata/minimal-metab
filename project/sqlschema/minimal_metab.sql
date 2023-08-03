

CREATE TABLE "AttributeValue" (
	has_raw_value TEXT, 
	type TEXT, 
	PRIMARY KEY (has_raw_value, type)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	type TEXT, 
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	has_raw_value TEXT, 
	PRIMARY KEY (type, has_unit, has_numeric_value, has_raw_value)
);

CREATE TABLE "SampleOperations" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SampleOperationsCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
