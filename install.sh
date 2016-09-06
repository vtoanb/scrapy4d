# Install commandline tools
xcode-select --install

# Install Homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install python 3
brew install python3

# Install virtualenv
pip3 install virtualenv

# Create virtual environment
virtualenv -p python3 ~/.scrapyEnv

# Install requirements
pip3 install -r ~/scrapy4d/crawl_4d/require.txt


