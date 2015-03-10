#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
 
#define BUFFER_SIZE (8 * 1024)
#define RET_GOTO(code, marker) \
	ret = code; \
	goto marker;
 
int read_key(char *keyfile, char **key, long *key_length)
{
	int ret = 0;
	FILE *fd;
 
	fd = fopen(keyfile, "rb");
	if(key == NULL) {
		return 1;
	}
	fseek(fd, 0, SEEK_END);
	*key_length = ftell(fd);
	fseek(fd, 0, SEEK_SET);
	*key = malloc(sizeof(char) * *key_length);
	fread(*key, sizeof(char), *key_length, fd);
	fclose(fd);
	return ret;
}
 
void xor(FILE *in, FILE *out, char *key, long key_length)
{
	char buf[BUFFER_SIZE];
	int i, n;
	long o = 0;
 
	while((n = fread(buf, sizeof(char), BUFFER_SIZE, in)) > 0) {
		for(i = 0; i < n; i++) {
			buf[i] ^= key[o];
			if(++o == key_length) {
				o = 0;
			}
		}
		fwrite(buf, sizeof(char), n, out);
	}
}
 
int main(int argc, char **argv)
{
	int ret = EXIT_SUCCESS;
	int c;
	char *_in = NULL;
	char *_key = NULL;
	char *_out = NULL;
	FILE *in = NULL;
	FILE *out = NULL;
	char *key = NULL;
	long key_length;
 
	while((c = getopt(argc, argv, "i:k:o:")) != -1) {
		switch(c) {
		case 'i':
			_in = optarg;
			break;
		case 'k':
			_key = optarg;
			break;
		case 'o':
			_out = optarg;
			break;
		default:
			printf("Usage: xor -i in -k key -o out\n");
			return EXIT_FAILURE;
		}
	}
	if(_in == NULL || _key == NULL || _out == NULL) {
		printf("Usage: xor -i in -k key -o out\n");
		return EXIT_FAILURE;
	}
 
	if(read_key(_key, &key, &key_length) != 0) {
		printf("error reading %s\n", _key);
		return EXIT_FAILURE;
	}
 
	in = fopen(_in, "rb");
	if(in == NULL) {
		printf("error opening %s\n", _in);
		RET_GOTO(EXIT_FAILURE, free_key);
	}
 
	out = fopen(_out, "wb");
	if(out == NULL) {
		printf("error opening %s\n", _out);
		RET_GOTO(EXIT_FAILURE, close_in);
	}
	xor(in, out, key, key_length);
 
	fclose(out);
close_in:
	fclose(in);
free_key:
	free(key);
 
	return ret;
}
