RST sample 
===================


*   https://docutils.sourceforge.io/docs/ref/rst/directives.html

* https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html


빈글문자에서 중심이 되는 문자는 표의문자이지만 비(非)표의문자도 사용할수 있다. 비표의문자에는 기능어, 쪽문자가 있다. 쪽문자는 의미에 있어서 중의적이며 상징적이다. 쪽문자는 점이 하나 붙으며 알파벳, 표음문자, 숫자에 해당한다.


.. https://stackoverflow.com/questions/44247102/reference-figures-in-restructuredtext-via-figure-numbers-using-numref

.. figure:: /_static/빈글의문자/b01-chars+c.png
    :scale: 50 %
    :alt: smartcity symbol
    :name: my-custom-label
    :align: center

    This is the caption of the figure (a simple paragraph).

    This is the legend of the figure

:numref:`my-custom-label`

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!
     
     



- Item 1, paragraph 1.

  Item 1, paragraph 2.

- Item 2.

name : string
    Customer name.
i : int
    Temporary index variable.



If [#a]_ is the first footnote reference, it will show up as
"[1]".  We can refer to it again as [#b]_ and again see
"[1]".  We can also refer to it as (an ordinary internal
hyperlink reference).

[#c]_

----

.. [#a] This is the footnote labeled "note".

.. [#b] This is the footnote labeled "note".

.. [#c]


:Hello: This field has a short field name, so aligning the field
        body with the first line is feasible.

:Number-of-African-swallows-required-to-carry-a-coconut: It would
    be very difficult to align the field body with the left edge
    of the first line.  It may even be preferable not to begin the
    body on the same line as the marker.


.. _Python: http://www.python.org

.. _example:

    asdajsdjajsd
    
.. |example|  replace::  123456 
    
.. [CIT2002] Just like a footnote, except the label is
   textual.

.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.
   
   
The "_example" target above points to this paragraph.

Paragraphs contain text and may contain inline markup:
*빈글*, **빈글**, `빈글`, ``빈글 문자``, standalone hyperlinks (http://www.python.org),
external hyperlinks (Python_), internal cross-references
(example_), footnote references ([1]_), citation references
([CIT2002]_), substitution references (|example|), and _`inline
internal targets`.




.. ::
    
    # dot -Tpng g02-.gv  -o g02-.png
    
    
..  graphviz::
    :align: center 
            
    Graph G 
    {
        layout=dot;
        fontname="gulim.ttc" ; 
        fontsize=9;
        rankdir="TB";
        node [shape=circle, fontname="gulim.ttc", fontsize=9];
        edge [fontname="gulim.ttc", fontsize=9];
        
        subgraph clusterD {
            margin=20;
            label = "<단어>" ;
            subgraph clusterA {
                margin=20;
                label = "<논리문자>" ;
                
                subgraph clusterB {
                  margin=20;
                  label = "<틀자>" ;
                  a;
                  b;
                  c;
                  
                  subgraph clusterB {
                    margin=20;
                    label = "<조합자>" ;
                    g;
                    
                  }
                  
                }
                
                subgraph clusterC {
                  margin=20;
                  label = "<무리자>" ;
                  m -- n;
                  o -- p -- q ;
                }
            }
            
            subgraph clusterE {
              margin=20;
              label = "<여러자>" ;
              x ; 
            }
                
        }
    }



