import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud

def get_word_cloud(text):
    """Get a word cloud for a text string
    
    Args:
        text: string for word cloud
    Returns:
        A WordCloud wordcloud object
    """
    return WordCloud(width=800,
                     height=400,
                     background_color=None,
                     mode='RGBA',
                     colormap='Wistia').generate(text)
    

def display_word_cloud(word_cloud):
    """Display a wordcloud object as an image

    Args:
        word_cloud: A WordCloud wordcloud object
    """
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def save_word_cloud(word_cloud, filename):
    """Save the wordcloud as a png file

    Args:
        word_cloud: A WordCloud wordcloud object
        filename: A string to name the png file.
    """
    word_cloud.to_file(f'{filename}.png')


def main():
    """Main function. Entry point of script
    """
    questions = ['Q1','Q2','Q3','Q4']

    df = pd.read_csv('survey_responses.csv')

    for q in questions:
        text =','.join(df[q])
        word_cloud = get_word_cloud(text)
        display_word_cloud(word_cloud)
        save_word_cloud(word_cloud, q)


if __name__ == '__main__':
    main()
