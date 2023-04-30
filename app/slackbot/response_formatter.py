from urllib.parse import unquote

def format_query_response_with_sources(response):
    answer = response.get('answer', '')
    sources = response.get('sources', '')

    sources_list = sources.split(',')
    file_names = [unquote(source.replace('.md', '').split('\\')[-1]) for source in sources_list]
    sources_text = '\n'.join([f"• <{file_name}|{file_name.split('/')[-1]}>" for file_name in file_names])
    formatted_response = f"{answer}\n\nSources:\n{sources_text}"

    return formatted_response
