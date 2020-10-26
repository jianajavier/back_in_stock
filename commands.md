# Commands

#### To simply compile and run

##### Build
`docker build -t back_in_stock`

##### Run
`docker run -v /Users/jianajavier/workspace/back_in_stock:/back_in_stock back_in_stock`

* The `-v /Users/jianajavier/workspace/back_in_stock:/back_in_stock` is crucial to the code that saves a screenshot when there is an error.
* See [docker volumes](https://docs.docker.com/storage/volumes/#start-a-service-with-volumes) for details

#### To interactively debug
`docker run -it -v /Users/jianajavier/workspace/back_in_stock:/back_in_stock back_in_stock`

* `-it` runs docker in interactive mode (interact with STDIN) and allocates a pseudo-TTY. See [docker run docs](https://docs.docker.com/engine/reference/commandline/run/) for more details
* See [pdb](https://docs.python.org/3/library/pdb.html) python documentation for python debugging details
