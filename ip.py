import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))