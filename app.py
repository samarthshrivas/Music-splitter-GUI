import streamlit as st
from spleeter_helper import separate_audio
from audio_helper import load_audio, create_audio_player, set_audio_volume
sample_rate = 44100

st.write('hello')
def main():
    st.title("Music Separator")

    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])
    if audio_file is not None:
        st.audio(audio_file, format="audio/mp3")
        if st.button("Separate"):
            components = separate_audio(audio_file)
            print(components)
            st.write(components)
            # audio_players = {}
            # for component_name, audio_data in components.items():
            #     st.write(component_name)
            #     print(component_name)
            #     st.audio(audio_data, sample_rate = sample_rate)
                # print(component_name)
                # audio_player_html = create_audio_player(audio_data, component_name)
                # audio_players[component_name] = st.components.v1.html(audio_player_html, width=500, height=50)


if __name__ == "__main__":
    main()


# import streamlit as st
# import base64
# from audio_helper import create_audio_player

# def main():
#     st.title("Music Splitter")

#     audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
#     if audio_file is not None:
#         st.audio(audio_file, format="audio/mp3")
#         if st.button("Separate"):
#             components = separate_audio(audio_file)

#             audio_players = ""
#             for i, component in enumerate(components):
#                 audio_players += create_audio_player(component, i)

#             st.components.v1.html(audio_players, width=500, height=200)

# if __name__ == "__main__":
#     main()
