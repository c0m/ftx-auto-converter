# FTX Auto Converter

## What is this for?
If you stake or lend out certain currencies or tokens on FTX, you will either be paid staking rewards or interest for your actions. This lets you convert all of these rewards and interest in to a token or currency of your choosing regularly, protecting you from market adjustments that might work against you if you do it all at once. 

## But why would I want to lend my token to shorts?
Because in some markets with low liquidity, rates can become extremely high for a period of time even without significant market movement. Consider when TomoChain briefly had 3600% annualised interest, and >100% interest for days after. TOMO longs could have lent their assets for 2% interest in just the 5 hours the interest rate spiked.  

![image](https://user-images.githubusercontent.com/61923663/134816465-dba669a8-08ec-4032-ab65-b0ff58c25b96.png)

You may not want to keep the interest you earn in this token though for a variety of reasons, maybe you don't want this extra added to your long position, maybe you want to supplement other long positions, maybe you want to keep in fiat. Whatever you want to do, this is why this repository exists. 

## So how does it work?
Before doing anything, set all currencies and tokens that you want to be targets for this to be loaned and set whatever interest rate you want, or stake them if applicable (e.g. SOL, SRM). This will make them not show up in your balance as available. **OTHERWISE THIS BALANCE WILL BE CONVERTED TO YOUR TARGET CURRENCY.** 

This is designed to run in a Docker container. Fill out the settings.py file with your API keys, subaccount (if applicable), which ticker you want to convert to, and which tickers you want to convert from. Every hour, it will check all of the available balances of the currencies you want to convert from and converts it in your your target currency.

## I want to add some stuff to this or want a feature
Absolutely feel free to open a pull request or open an issue

## Is this financial advice or does this repository come with any warranty?
![image](https://user-images.githubusercontent.com/61923663/134817256-d95af51f-1866-4e66-9c24-28313d3e264d.png)
