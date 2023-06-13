<script>
  import { ALLWORDS } from './assets/all_words';
  import { HARD } from './assets/hrd'
  import { WORDS } from './assets/words';


  import KeyBoard from './lib/KeyBoard.svelte';
  import LetterRow from './lib/LetterRow.svelte';
  import LetterRowBlank from './lib/LetterRowBlank.svelte';
  import LetterRowEdit from './lib/LetterRowEdit.svelte';
  
  let difficulty='easy'
  let guesses=[]
  let correct = newWord()
  let num_guesses_left=7
  let green = ''
  let yellow = ''
  let dark = ''
  let num_won=0

  $: difficulty && guesses.length && newWord()
  
  function newWord(){
    let word 
    if (difficulty == 'hard'){
        word = ALLWORDS[Math.floor(Math.random()*ALLWORDS.length)]
    }else if (difficulty == 'extreme'){
      word = HARD[Math.floor(Math.random()*HARD.length)]
    }else{
      word = WORDS[Math.floor(Math.random()*WORDS.length)]
    }
    if (guesses.includes(word)){
      return newWord()
    }
    return word
  }
  function checkWord(word){
    let tmpguesses=guesses
    tmpguesses.push(word)
    guesses= tmpguesses

    if (correct===word){
      num_won+=1
      setTimeout(()=>{
        green=''
        yellow=''
        dark=''
        correct = newWord()
      },500)
    }
    else num_guesses_left -=1
    if(num_guesses_left==0) alert("You lost with "+correct)
  }
  function addGreen(s){
    green = String.prototype.concat(...new Set(green+=s))
  }
  function addYellow(s){
    yellow+=s
  }
  function addDark(s){
    dark+=s
  }
  $:hideYellow = guesses[-1]!=correct && num_won>5 && green.length>=5
</script>

<div class='header'>
  <div class='score'>score: {num_won}</div>
  <h1 class='title'>InfinitLE</h1>
  <div class='radios'>
    <label>
      <input type=radio bind:group={difficulty} name="scoops" value={'easy'}>
      Normal
    </label>
    
    <label>
      <input type=radio bind:group={difficulty} name="scoops" value={'difficult'}>
      Difficult
    </label>
    
    <label>
      <input type=radio bind:group={difficulty} name="scoops" value={'extreme'}>
      Extreme
    </label>
  </div>

</div>
<div class="num-won">{num_won}</div>
<div style='height:60px' />
<div id='game-board'>
  {#key correct}
    {#each guesses as word}
      <LetterRow {word} {correct} test={true} {addDark} {addGreen} {addYellow} hidegrey={num_won>5} hideyellow={hideYellow}/>
    {/each}
  {/key}
  {#if num_guesses_left>0}
    <LetterRowEdit on:check={(e)=>checkWord(e.detail)}/>
    {#each [...Array(num_guesses_left-1)] as i}
      <LetterRowBlank />
    {/each}
  {/if}
</div>
<KeyBoard bind:green bind:yellow bind:dark/>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Kolker+Brush&display=swap');
  h1 {
    text-align: center;
  }
  
  #game-board {
    display: flex;
    align-items: center;
    flex-direction: column;
  }
  .num-won{
    position: absolute;
    z-index: -20;
    font-family: 'Kolker Brush', cursive;
    font-size: 600px;
    color: rgba(96, 101, 180, 0.4);
    bottom: 50%;
    right:10%;
  }
  .header{
    position:absolute;
    top:0;
    left:0;
    width: 100%;
    box-shadow: 0px 0px 4px grey;
  }
  .score{
    position: absolute;
    left:0;
    padding: 16px;
    padding-left: 52px;
    font-family: 'Kolker Brush', cursive;
    font-size: 40px;
  }
  .title{
    left:50%;
    margin: 8px;
  }
</style>
