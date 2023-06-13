<script>
    import { createEventDispatcher } from 'svelte'
    import { ALLWORDS } from "../assets/all_words";

	
    let word = ''
    
    const dispatch = createEventDispatcher()
    $: notfound = (word.length==5 && !ALLWORDS.includes(word)) ? true : false
    $: classBasic = notfound ? "letter-box filled-box red":"letter-box filled-box"
    
    function insertLetter(e){
        if (word.length==5) return
        word+=e
    }
    function deleteLetter(){
        word = word.slice(0,-1)
    }
    function handleKeyUp(e){
        let pressedKey = String(e.key)
        if (pressedKey === "Backspace" || pressedKey === "Del" ) {
            deleteLetter()
            return
        }
    
        if (pressedKey === "Enter" && ALLWORDS.includes(word)) {
            dispatch('check',word)
            word=''
            return
        }
    
        let found = pressedKey.match(/[a-z]/gi)
        if (!found || found.length > 1) {
            return
        } else {
            insertLetter(pressedKey)
        }
      }
    document.addEventListener("keyup", handleKeyUp)
</script>

<div class="letter-row">
    {#key word}
        <div class={classBasic} >{word[0] ?? ''}</div>
        <div class={classBasic} >{word[1] ?? ''}</div>
        <div class={classBasic} >{word[2] ?? ''}</div>
        <div class={classBasic} >{word[3] ?? ''}</div>
        <div class={classBasic} >{word[4] ?? ''}</div>
    {/key}
</div>

<style>
    .red {
        color:red;
    }

    .filled-box {
        border: 2px solid black;
    }

    .letter-row {
        display: flex;
    }

    .letter-box {
        border: 2px solid rgb(96, 101, 180);
        border-radius: 3px;
        margin: 2px;
        font-size: 2rem;
        font-weight: 700;
        height: 3rem;
        width: 3rem;
        display: flex;
        justify-content: center;
        align-items: center;
        text-transform: uppercase;
    }
</style>