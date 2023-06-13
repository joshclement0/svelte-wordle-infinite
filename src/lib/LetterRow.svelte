<script>
    export let word = '     '
    export let correct = 'green'
    export let test = false
    export let hideyellow = false
    export let hidegrey = false
    export let addGreen=(s)=>{}
    export let addYellow=(s)=>{}
    export let addDark=(s)=>{}

    const classGreen = "letter-box filled-box green"
    const classYellow = "letter-box filled-box yellow"
    const classBasic = "letter-box filled-box grey"

    let letterColors=['grey','grey','grey','grey','grey']
    function classFromLetter(){
        if(!test) return classBasic
        let answer = correct
        const colors = Array(word.length).fill('grey');
        // loop through guess and mark green if fully correct
        for (let i = 0; i < word.length; i++) {
            if (word[i] === answer[i]) {
                colors[i] = "green";
                // remove letter from answer, so it's not scored again
                answer = answer.replace(word[i], " ");
            }
        }
        // loop through guess and mark yellow if partially correct
        for (let i = 0; i < word.length; i++) {
            if (colors[i] !== "green" && answer.includes(word[i])) {
                colors[i] = "yellow";
                // remove letter from answer, so it's not scored again
                answer = answer.replace(word[i], " ");
            }
        }
        letterColors =colors
        for(let i = 0;i<word.length;i++){
            if (colors[i]=='green'){
                addGreen(word[i])
            }else if (colors[i]=='yellow'){
                addYellow(word[i])
            }else{
                addDark(word[i])
            }
        }
    }
    let classMap={
        'grey':classBasic,
        'green':classGreen,
        'yellow':classYellow
    }
    classFromLetter()
    $: classes = letterColors.map((e)=>classMap[e])
    $: toHide = (hidegrey && letterColors[0]=='grey' && letterColors[1]=='grey' && letterColors[2]=='grey' && letterColors[3]=='grey' && letterColors[4]=='grey') ||
            (hideyellow && letterColors[0]!='green' && letterColors[1]!='green' && letterColors[2]!='green' && letterColors[3]!='green' && letterColors[4]!='green')

</script>
{#if !toHide}
<div class="letter-row">
    <div class={classes[0]} >{word[0]}</div>
    <div class={classes[1]} >{word[1]}</div>
    <div class={classes[2]} >{word[2]}</div>
    <div class={classes[3]} >{word[3]}</div>
    <div class={classes[4]} >{word[4]}</div>
</div>
{/if}

<style>
    .grey{
        background-color: rgb(144, 142, 142);
        color:black;
    }
    .green {
        background-color: lightgreen;
        color:black;
    }
    .yellow {
        background-color: #ff9;
        color:black;
    }
    .filled-box {
        border: 2px solid black;
    }

    .letter-row {
        display: flex;
    }

    .letter-box {
        border: 2px solid gray;
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