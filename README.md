# green_office

## System description 

**green_office** is a project thought to save our office from pollution and excessive urbanization. We want our wonderful plants to grow up and be green, even though we don't have green thumb. What is better than an automatic irrigation system to make them be every day greener than the day before?
We would like to check if they need water when we're on holiday too (we don't want them to die), we need to be able to control our automatic irrigation system remotely.
But wait, what if someone wants to make our plants die? We'd cry :'(
Solution: it's necessary to implement a security system in our IoT project! :D

## Possible future development
Moreover it would be a good idea to collect acquired data (humidity for example) in a DB through NodeRED and Raspberry Pi

More specifically, 
1. acquires data from humidity sensors,
2. makes irrigation system works,
3. understands when (after how many days) the plants need water (how much water?)
4. generates one or more tokens that allows the listeners to un-hide the image of the speaker

The [specification](https://en.wikipedia.org/wiki/Specification_(technical_standard)) of the system is 
given by the requirements collected in the [requirements directory](./requirements).

## Secure System Engineering Process

1. use the [clone (& branch) & pull request workflow](https://guides.github.com/introduction/flow/)
2. follow the diagram depicted below (and available [here](./designs/methodology-activity-UML.png), in the design directory)
	1. create your branch (use the name of your github account)
	2. review the functional requirements [here](./requirements/1-functional-requirements.md)
	3. open a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) from your branch to the master
	4. implement or design a (partial/draft) solution for the requirements
	5. test your solution, providing the details with the outcome and how to reproduce the test [here](./tests)
	6. introduce mitigations if needed
	7. restart from 1. with the security requirements
