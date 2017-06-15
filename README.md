This project is a spack repository of packages developed or customized for 
USGS Astrogeology Science Center. 

In order to add an addtional repository to spack and use these packages do the following:

1. create a repos.yaml file and place it in:
	* $spack/etc/spack/ to override your local spack install
	* ~/.spack/ to create just for your user.
	
    The contents of this file should look like:
    ```
    repos:
      - /path/to/local-repo
      - $spack/var/spack/repos/builtin
    ```
    
    The order of repos establishes precedence and ordering allowing you to overrride the builtin packages with customizations

2. Then clone this repo to the location you've specfied in the repos.yaml file above. 

    Check that this is working with `spack repos list`

For more docs on spack repos see: [https://spack.readthedocs.io/en/latest/repositories.html#](https://spack.readthedocs.io/en/latest/repositories.html#)
