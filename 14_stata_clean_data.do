* Import csv file
* need to know demiliter is comma or |, if different from comma use option
import delimited "data\raw\european_commission\ted-sample.csv", clear

* Only keep relevant variables
keep iso_country_code win_country_code award_value_euro

* Summarize award_value_euro
summarize award_value_euro
summarize award_value_euro, detail

* see bottom of documentation of 'summarize' command there is SCALARS 
* it is local macro
help summarize

* you can see total number of observations
display `r(N)'
display "Number of observation: `r(N)'"
display "Mean: `r(mean)'"

* Let's generate an indicator: 1(above mean), 0 otherwise
* you can use local macro
generate above_mean = 1
replace above_mean = 0 if award_value_euro < `r(mean)' 
tab above_mean

*generate above_median = 1
*replace above_median = 0 if award_value_euro < `r(p50)'
*tab above_median

generate above_median = (award_value_euro > `r(p50)')

* Drop outliers
drop if award_value_euro > `r(p95)'
histogram award_value_euro


* Little excursion: Looping in Stata

************************************
* Recall Python loop syntax: not include 10
* for i in range(10):
*	print(i)
************************************

* forvalues loop
forvalues i = 0/9 {
	display `i'
}

* foreach (1) loop 
* be careful if not use `', displayd 3 times of just word "vegetable"
foreach vegetable in paprika carrot onion {
	display "`vegetable'"
}

* foreach (2) loop 
foreach var of varlist iso_country_code win_country_code award_value_euro {
	count if strlen(`var') > 2
}













