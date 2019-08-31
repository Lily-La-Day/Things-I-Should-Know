

const width = 1000

const init = () => {

  const makeGrid = () => {

    for(let i = 0; i < width * width; i ++ ) {
      const grid = document.querySelector('.grid')
      const square = document.createElement('div')
      grid.append(square)
      square.classList.add('grid-item')


    }
  }
  makeGrid()
}


window.addEventListener('DOMContentLoaded', init)
